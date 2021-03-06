#!/usr/bin/env python

from sys import argv

if len(argv) < 3:
    print("Usage: freeStreamingShell.py sample_file sample_format_file")
    exit(-1)

import assignmentFormat
import freeStreaming

sample_filename = argv[1]
sample_format_filename = argv[2]
#sample_filename = "/home/qiu/Downloads/fancy_movie/results/samples_211.dat"
#sample_format_filename = "/home/qiu/Downloads/fancy_movie/results/samples_format.dat"

ordered_streaming_filename = "results/streaming_particle3d.dat"
streaming_format_filename = "results/streaming_particle3d_format.dat"

from parameters_freeStreaming import time_interval, starting_time, particle_endding_time, coordinate_xy_boundary, coordinate_z_boundary

sample_format_dict = assignmentFormat.assignmentExprStream2IndexDict(file(sample_format_filename))

streaming_format_dict = freeStreaming.freeStreaming3d(
    file(sample_filename), sample_format_dict, file(ordered_streaming_filename, "w"),
    starting_time=starting_time, endding_time=particle_endding_time,
    time_interval=time_interval,
    coordinate_xy_boundary=coordinate_xy_boundary,
    coordinate_z_boundary=coordinate_z_boundary,
    )

streaming_format_file = file(streaming_format_filename,"w")
for aTerm in assignmentFormat.dict2AssignmentExprList(streaming_format_dict):
    streaming_format_file.write(aTerm + "\n")
streaming_format_file.close()
