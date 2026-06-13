import pytest
from viral_optimizer import ViralOptimizer, Thumbnail

def test_generate_thumbnails():
    optimizer = ViralOptimizer()
    video_title = "Test Video"
    video_transcript = "This is a test video"
    thumbnails = optimizer.generate_thumbnails(video_title, video_transcript)
    assert len(thumbnails) == 3
    for thumbnail in thumbnails:
        assert isinstance(thumbnail, Thumbnail)

def test_overlay_text():
    optimizer = ViralOptimizer()
    thumbnail = Thumbnail("thumbnail.jpg", "Test Thumbnail")
    font_size = 12
    contrast = 4.5
    overlaid_text = optimizer.overlay_text(thumbnail, font_size, contrast)
    assert overlaid_text.startswith(thumbnail.text)

def test_select_thumbnail():
    optimizer = ViralOptimizer()
    thumbnails = [Thumbnail("thumbnail1.jpg", "Test Thumbnail 1"), Thumbnail("thumbnail2.jpg", "Test Thumbnail 2")]
    selected_thumbnail = optimizer.select_thumbnail(thumbnails)
    assert selected_thumbnail in thumbnails

def test_store_thumbnail():
    optimizer = ViralOptimizer()
    thumbnail = Thumbnail("thumbnail.jpg", "Test Thumbnail")
    video_metadata = {}
    optimizer.store_thumbnail(thumbnail, video_metadata)
    assert "thumbnail_url" in video_metadata
