// static/js/content_loader.js
class ContentLoader {
    constructor() {
        this.contentGrid = document.querySelector('.content-grid');
        this.loadingState = false;
    }

    async fetchContent(type = 'recommended') {
        if (this.loadingState) return;

        this.loadingState = true;
        this.showLoader();

        try {
            const response = await fetch(`/api/content/fetch?type=${type}`);
            const data = await response.json();

            this.renderContent(data);
        } catch (error) {
            console.error('Error fetching content:', error);
            this.showError();
        } finally {
            this.loadingState = false;
            this.hideLoader();
        }
    }

    renderContent(content) {
        this.contentGrid.innerHTML = content.map(item => `
            <div class="content-card">
                <h3>${item.title}</h3>
                <p>${item.description}</p>
                <div class="card-footer">
                    <span class="content-type">${item.content_type}</span>
                    <a href="${item.url}" class="btn-primary" target="_blank">
                        View Content
                    </a>
                </div>
            </div>
        `).join('');
    }

    showLoader() {
        this.contentGrid.innerHTML = '<div class="loader">Loading...</div>';
    }

    hideLoader() {
        const loader = this.contentGrid.querySelector('.loader');
        if (loader) loader.remove();
    }

    showError() {
        this.contentGrid.innerHTML = `
            <div class="error-message">
                Failed to load content. Please try again.
            </div>
        `;
    }
}

// Initialize content loader
document.addEventListener('DOMContentLoaded', () => {
    const loader = new ContentLoader();
    loader.fetchContent();

    // Set up navigation listeners
    document.querySelectorAll('.side-nav a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const type = e.target.getAttribute('href').slice(1);
            loader.fetchContent(type);
        });
    });
});