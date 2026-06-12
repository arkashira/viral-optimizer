import pytest
import os
from viral_optimizer import ViralOptimizer, Thumbnail

def test_generate_thumbnails():
    viral_optimizer = ViralOptimizer()
    video_title = "Example Video"
    video_transcript = "This is an example video transcript."
    thumbnails = viral_optimizer.generate_thumbnails(video_title, video_transcript)
    assert len(thumbnails) == 3
    for thumbnail in thumbnails:
        assert thumbnail.width == 1280
        assert thumbnail.height == 720

def test_optimize_text_overlay():
    viral_optimizer = ViralOptimizer()
    video_title = "Example Video"
    video_transcript = "This is an example video transcript."
    text_overlay = viral_optimizer.optimize_text_overlay(video_title, video_transcript)
    assert text_overlay == f"{video_title}\n{video_transcript}"

def test_save_thumbnail():
    viral_optimizer = ViralOptimizer()
    thumbnail_url = "thumbnail.jpg"
    text_overlay = "Example text overlay"
    viral_optimizer.save_thumbnail(thumbnail_url, text_overlay)
    assert os.path.exists(thumbnail_url)
    os.remove(thumbnail_url)  # Clean up

def test_get_thumbnail_urls():
    viral_optimizer = ViralOptimizer()
    thumbnails = [Thumbnail("thumbnail1.jpg", 1280, 720), Thumbnail("thumbnail2.jpg", 1280, 720)]
    thumbnail_urls = viral_optimizer.get_thumbnail_urls(thumbnails)
    assert thumbnail_urls == ["thumbnail1.jpg", "thumbnail2.jpg"]

def test_validate_thumbnails():
    viral_optimizer = ViralOptimizer()
    thumbnails = [Thumbnail("thumbnail1.jpg", 1280, 720), Thumbnail("thumbnail2.jpg", 1280, 720)]
    assert viral_optimizer.validate_thumbnails(thumbnails)

def test_validate_contrast_ratio():
    viral_optimizer = ViralOptimizer()
    thumbnails = [Thumbnail("thumbnail1.jpg", 1280, 720), Thumbnail("thumbnail2.jpg", 1280, 720)]
    assert viral_optimizer.validate_contrast_ratio(thumbnails)

def test_api_response():
    viral_optimizer = ViralOptimizer()
    thumbnails = [Thumbnail("thumbnail1.jpg", 1280, 720), Thumbnail("thumbnail2.jpg", 1280, 720)]
    api_response = viral_optimizer.api_response(thumbnails)
    assert api_response == '{"thumbnails": ["thumbnail1.jpg", "thumbnail2.jpg"]}'
