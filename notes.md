
# task1
the `soochak_message_all_values` table has things like p15 and p3
..but nothing about g14 and g3 like they said the email
seems like this is the right table..

looking at the param definitions..what's in the doc isn't right
  - or I don't understand what the doc is trying to say

p1 is machine id
p15 is pre pressure
p16 is post pressure
p17 is error code
p29 is enable/disable 1
p30 is enable/disable 2
p59 is enable/disable 3

enable/disable comes in as hex and has to be taken to binary
error comes in as hex, has to be taken to binary..
 - doesn't seem to be what ronak is saying
 - ended up just translating the errors to their corresponding table



# task 2
frm-master rows have:
 - time spent
 - date
 - franchisee participation
 - place-id (links to ro plant id?)

ro-plant has 
 - account ID
 - machineID

frm-activity-master
 - activity type (like "launch")

report-data
 - machine ID
 - production that day


accuont data in RO plant
particp data in frm master
prod data in soochak report data
..no idea what to join to get the appropriate data


water produced is unclear
 - not sure how to combine the soochak report data cols
 - will show water consumed as a placeholder instead
