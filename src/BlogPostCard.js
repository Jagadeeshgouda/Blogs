import React from 'react';
import { MEDIA_URL } from './constants';  // Adjust the path based on your project structure

function BlogPostCard({ post }) {
  const { title, description, content_type, media_file } = post;
  const mediaUrl = `http://127.0.0.1:8000${MEDIA_URL}${media_file}`;

  return (
    <div className="blog-post-card">
      <h2>{title}</h2>
      <p>{description}</p>
      {content_type === 'image' ? (
        <img src={mediaUrl} alt={title} />
      ) : content_type === 'video' ? (
        <video controls width="300" height="200">
          <source src={mediaUrl} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      ) : null}
    </div>
  );
}

export default BlogPostCard;