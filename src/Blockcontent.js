import React, { useState, useEffect } from "react";
import axios from "axios";

const BlogContentList = ({ blogPostId }) => {
  const [blogContent, setBlogContent] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/blogcontent/${blogPostId}/`)
      .then((response) => {
        console.log("Blog Content API Response:", response.data);
        setBlogContent(response.data);
      })
      .catch((error) => console.error("Error fetching blog content:", error));
  }, [blogPostId]);

  return (
    <div style={{ display: "flex", flexWrap: "wrap" }}>
      {blogContent !== null && (
        <div>
          {blogContent.content_type === "image" && (
            <img
              src={blogContent.media_file}
              alt="Image"
              style={{ width: 380, height: 300 }}
            />
          )}

          {blogContent.content_type === "video" && (
            <video width="380" height="300" controls>
              <source
                src={blogContent.media_file}
                type="video/mp4"
              />
              Your browser does not support the video tag.
            </video>
          )}
        </div>
      )}
    </div>
  );
};

export default BlogContentList;
