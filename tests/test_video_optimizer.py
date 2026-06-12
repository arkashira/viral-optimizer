from video_optimizer import VideoOptimizer, VideoPerformance

def test_add_video():
    optimizer = VideoOptimizer()
    optimizer.add_video("video1", 100, 50, 0.5)
    assert optimizer.get_video_performance("video1") == VideoPerformance(100, 50, 0.5)

def test_filter_videos():
    optimizer = VideoOptimizer()
    optimizer.add_video("video1", 100, 50, 0.5)
    optimizer.add_video("video2", 200, 100, 0.6)
    filtered_videos = optimizer.filter_videos("views", 150)
    assert len(filtered_videos) == 1
    assert list(filtered_videos.keys())[0] == "video2"

def test_sort_videos():
    optimizer = VideoOptimizer()
    optimizer.add_video("video1", 100, 50, 0.5)
    optimizer.add_video("video2", 200, 100, 0.6)
    sorted_videos = optimizer.sort_videos("views")
    assert len(sorted_videos) == 2
    assert sorted_videos[0][0] == "video2"

def test_compare_video_performance():
    optimizer = VideoOptimizer()
    optimizer.add_video("video1", 100, 50, 0.5)
    optimizer.add_video("video1_2022-01-01", 50, 25, 0.25)
    comparison = optimizer.compare_video_performance("video1", "2022-01-01")
    assert comparison == {"views": 50, "engagement": 25, "click_through_rate": 0.25}
