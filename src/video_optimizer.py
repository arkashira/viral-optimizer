import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class VideoPerformance:
    views: int
    engagement: int
    click_through_rate: float

class VideoOptimizer:
    def __init__(self):
        self.videos = {}

    def add_video(self, video_id, views, engagement, click_through_rate):
        self.videos[video_id] = VideoPerformance(views, engagement, click_through_rate)

    def get_video_performance(self, video_id):
        return self.videos.get(video_id)

    def filter_videos(self, metric, threshold):
        return {video_id: performance for video_id, performance in self.videos.items() if getattr(performance, metric) >= threshold}

    def sort_videos(self, metric):
        return sorted(self.videos.items(), key=lambda x: getattr(x[1], metric), reverse=True)

    def compare_video_performance(self, video_id, previous_date):
        current_performance = self.get_video_performance(video_id)
        previous_performance = self.get_video_performance(f"{video_id}_{previous_date}")
        if current_performance and previous_performance:
            return {
                "views": current_performance.views - previous_performance.views,
                "engagement": current_performance.engagement - previous_performance.engagement,
                "click_through_rate": current_performance.click_through_rate - previous_performance.click_through_rate
            }
        return None
