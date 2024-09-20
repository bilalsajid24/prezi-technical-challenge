/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export",
  reactStrictMode: true,
  swcMinify: true,
  eslint: {
    dirs: ["src"],
  },
  pageExtensions: ["page.tsx", "page.ts"],
  // Build fails if image optimization is enabled (Client-Side Rendering)
  images: {
    unoptimized: true,
    domains: ["localhost"],
  },
};

module.exports = nextConfig;
