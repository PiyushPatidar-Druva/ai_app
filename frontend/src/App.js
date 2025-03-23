import React, { useState } from 'react';
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Paper,
  CircularProgress,
  Alert,
} from '@mui/material';
import axios from 'axios';

function App() {
  const [story, setStory] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [videoPath, setVideoPath] = useState('');

  const handleGenerateVideo = async () => {
    try {
      setLoading(true);
      setError('');
      setSuccess('');
      
      const response = await axios.post('http://localhost:5000/api/generate-video', {
        story,
      });

      if (response.data.success) {
        setVideoPath(response.data.video_path);
        setSuccess('Video generated successfully!');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred while generating the video.');
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadVideo = () => {
    window.location.href = `http://localhost:5000/api/download-video?video_path=${videoPath}`;
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          AI Story to Video Converter
        </Typography>

        <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
          <Typography variant="h6" gutterBottom>
            Enter Your Story
          </Typography>
          
          <TextField
            fullWidth
            multiline
            rows={6}
            variant="outlined"
            value={story}
            onChange={(e) => setStory(e.target.value)}
            placeholder="Enter your story here..."
            sx={{ mb: 2 }}
          />

          <Button
            variant="contained"
            color="primary"
            onClick={handleGenerateVideo}
            disabled={loading || !story}
            fullWidth
            sx={{ mb: 2 }}
          >
            {loading ? <CircularProgress size={24} /> : 'Generate Video'}
          </Button>

          {videoPath && (
            <Button
              variant="contained"
              color="secondary"
              onClick={handleDownloadVideo}
              fullWidth
            >
              Download Video
            </Button>
          )}
        </Paper>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {success && (
          <Alert severity="success" sx={{ mb: 2 }}>
            {success}
          </Alert>
        )}
      </Box>
    </Container>
  );
}

export default App;
