import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BlogContentList from './Blockcontent';
import Navbar from './Navbar';  // Import the Navbar component
import Footers from "./Footers";
import { Router } from 'react-router-dom';

const BlogPostList = () => {
  const [blogPosts, setBlogPosts] = useState([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/blogposts/')
      .then(response => setBlogPosts(response.data))
      .catch(error => console.error('Error fetching blog posts:', error));
  }, []);

  return (
    <div>
      {/* Include the Navbar component */}
      <Navbar />
      
      
      {/* Rest of your BlogPostList component */}
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
        {blogPosts.map(blogPost => (
          <div key={blogPost.id} style={cardStyle}>
            <h4> {blogPost.user}</h4>
            <hr />
            <h5>{blogPost.title}</h5>
            <p>{blogPost.description}</p>
            <BlogContentList blogPostId={blogPost.id} />
          </div>
        ))}
      </div>
      <Footers/>
    </div>
  );
};

const cardStyle = {
  border: '2px solid #ccc',
  padding: '10px',
  margin: '16px',
  borderRadius: '15px',
  width: '90%',
  maxWidth: '400px',
};
<Footers/>

export default BlogPostList;
