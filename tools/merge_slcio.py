import os
from pyLCIO import IOIMPL, IMPL, EVENT

# Define input directory and output file path
input_dir = "reco/"
output_file = "reco/output_reco_run100.slcio"

# Create an LCWriter instance for the output file
writer = IOIMPL.LCFactory.getInstance().createLCWriter()
writer.open(output_file)

# Dictionary to store events (optional, used here to follow the given structure)
events = {}
global_event_index = 0

# Get a sorted list of all .slcio files in the input directory
input_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".slcio")])
evt_number_iterator = 0

# Loop over each input file
for file in input_files:
    file_path = os.path.join(input_dir, file)
    print(f"Processing file: {file_path}")
    
    # Create a reader instance and open the current file
    reader = IOIMPL.LCFactory.getInstance().createLCReader()
    reader.open(file_path)
    
    # Loop through each event in the current file
    for event in reader:
        print(f"Processing Event: {event.getEventNumber()} from file: {file}")
        
        # Create a new event and copy metadata
        events[global_event_index] = IMPL.LCEventImpl()
        events[global_event_index].setEventNumber(evt_number_iterator)
        evt_number_iterator += 1
        events[global_event_index].setRunNumber(event.getRunNumber())
        events[global_event_index].setTimeStamp(event.getTimeStamp())
        
        # List of collections to keep
        collections_to_keep = ["PandoraPFOs", "MCParticle"]
        
        # Copy only the desired collections from the event
        for collection_name in collections_to_keep:
            try:
                collection = event.getCollection(collection_name)
                events[global_event_index].addCollection(collection, collection_name)
            except EVENT.DataNotAvailableException:
                print(f"Warning: Collection '{collection_name}' not found in event {event.getEventNumber()} from file: {file}")
        
        # Write the new event to the output file
        writer.writeEvent(events[global_event_index])
        global_event_index += 1
    
    # Close the reader for the current file
    reader.close()

# Close the writer after all events have been processed
writer.close()

print(f"Merged file saved as '{output_file}' with {global_event_index} events.")

