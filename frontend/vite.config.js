import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';
import banner from "vite-plugin-banner";
import pkg from './package.json'

const BANNER_TEXT = `/**
* name: ${pkg.name} 
* version: ${pkg.version}
*/`;

export default defineConfig({
    plugins: [
        vue({
            include: [/\.vue$/, /\.md$/],
        }),
        banner(BANNER_TEXT),
    ],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
        //extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json', '.vue'], //should not use
    },
    server: {
        host: "localhost",
        port: 9000,
        proxy: {
            "/api": {
                target: "http://localhost:5000",
                changeOrigin: false,
                secure: false,
                protocolRewrite: 'http',
                rewrite: (path) => path.replace(/^\/api/, ""),
            },
        },
    },
});