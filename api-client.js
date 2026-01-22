// 🔌 API Integration Layer - ใช้แทน Direct Supabase
const API = {
    baseURL: '/api',
    
    // ✅ License endpoints
    async activateLicense(licenseKey, accountId, hwid) {
        const res = await fetch(`${this.baseURL}/license/activate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ license_key: licenseKey, account_id: accountId, hwid: hwid })
        });
        return res.json();
    },
    
    async verifyLicense(licenseKey, hwid) {
        const res = await fetch(`${this.baseURL}/license/verify`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ license_key: licenseKey, hwid: hwid })
        });
        return res.json();
    },
    
    async deactivateLicense(licenseKey) {
        const res = await fetch(`${this.baseURL}/license/deactivate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ license_key: licenseKey })
        });
        return res.json();
    },
    
    async resetHWID(licenseKey) {
        const res = await fetch(`${this.baseURL}/license/reset-hwid`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ license_key: licenseKey })
        });
        return res.json();
    },
    
    // ✅ Auth endpoints
    async login(email, password) {
        const res = await fetch(`${this.baseURL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });
        return res.json();
    },
    
    async verifyToken(token) {
        const res = await fetch(`${this.baseURL}/auth/verify`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` }
        });
        return res.json();
    },
    
    // ✅ Health check
    async health() {
        const res = await fetch(`${this.baseURL}/health`);
        return res.json();
    }
};

// 📝 Usage example:
// const result = await API.verifyLicense('license-123', 'hwid-456');
// const login = await API.login('admin@example.com', 'password');
