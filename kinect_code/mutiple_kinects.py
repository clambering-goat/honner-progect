num_devices = freenect.num_devices(ctx)

while True:
    depth_frames = [freenect.sync_get_depth(i) for i in range(num_devices)]
    video_frames = [freenect.sync_get_video(i) for i in range(num_devices)]

freenect.sync_stop()
