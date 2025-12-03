function theme(){
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'dark') {
            themeToggleBtn.checked = true;
        }
    }
}

    themeToggleBtn.addEventListener('change', function(event){
        if (event.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }
    });
    document.addEventListener('DOMContentLoaded', function() {
        theme();
    });
    const themeToggleBtn = document.getElementById('theme-toggle-btn');

    function load_posts(){
        fetch('/posts')
        .then(response => response.json())
        .then(data => {
            const postsContainer = document.getElementById('posts-container');
            postsContainer.innerHTML = '';
            data.posts.forEach(post => {
                const postElement = document.createElement('div');
                postElement.className = 'post';
                postElement.innerHTML = `
                    <h2>${post.title}</h2>
                    <p>${post.content}</p>
                    <span>By ${post.author} on ${new Date(post.timestamp).toLocaleString()}</span>
                `;
                postsContainer.appendChild(postElement);
            });
        });
    }


    function post_zoom_in(postId) {
        const postElement = document.getElementById(`post-${postId}`);
        postElement.classList.add('zoomed-in');
    }
