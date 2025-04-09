from pyLCIO import IOIMPL, IMPL, EVENT

# Input and output file paths
input_file = "output_reco.slcio"
output_file = "trimmed_output.slcio"

# Create LCReader and LCWriter instances
reader = IOIMPL.LCFactory.getInstance().createLCReader()
writer = IOIMPL.LCFactory.getInstance().createLCWriter()

# Open the input and output files
reader.open(input_file)
writer.open(output_file)

# Dictionary to store events
events = {}

# Loop through events in the input file
for event_index, event in enumerate(reader):
    
    #to cap events if necessary
    #if event_index > 9:
        #break

    print(f"Processing Event: {event.getEventNumber()}")

    # Create a new event and copy metadata
    events[event_index] = IMPL.LCEventImpl()
    events[event_index].setEventNumber(event.getEventNumber())
    events[event_index].setRunNumber(event.getRunNumber())
    events[event_index].setTimeStamp(event.getTimeStamp())

    # List of collections to keep
    collections_to_keep = ["PandoraPFOs", "MCParticle"]

    # Copy only the desired collections
    for collection_name in collections_to_keep:
        try:
            collection = event.getCollection(collection_name)
            events[event_index].addCollection(collection, collection_name)
        except EVENT.DataNotAvailableException:
            print(f"Warning: Collection '{collection_name}' not found in event {event.getEventNumber()}")

    # Write the new event to the output file
    writer.writeEvent(events[event_index])

# Close the reader and writer
reader.close()
writer.close()

print(f"Trimmed file saved as '{output_file}'")

