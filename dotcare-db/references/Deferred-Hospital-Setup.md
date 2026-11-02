# Deferred hospital setup

Hospital setup migration is deferred at the user's request. When that work starts, trace each combination of `HSM.HSAssigment.AssignmentTypeID` and `AssignmentClassificationID` through the native integration workflow. Those assignments determine which module caches must be created or updated. Do not apply one universal cache-copy rule to all hospital structures.

Warehouse setup is the current implementation priority. No hospital-structure or hospital-assignment migration is enabled by this warehouse work.
