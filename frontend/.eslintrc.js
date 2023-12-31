module.exports = {
  root: true,
  // env: {
  //   //node: true,
  //   es2021: true,
  // },
  parserOptions: {
    "ecmaVersion": 2021
  },
  globals: {
    defineProps: "readonly",
    defineEmits: "readonly",
    defineExpose: "readonly"
  },
  extends: [
    "plugin:vue/vue3-essential",
    "eslint:recommended",
    "@vue/typescript/recommended",
    "@vue/prettier",
    "@vue/prettier/@typescript-eslint",
  ],
  parserOptions: {
    ecmaVersion: 2020,
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "prettier/prettier": ["error", { "endOfLine": "auto" }],
    'prettier/prettier': 0,
  },
  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)",
      ],
      env: {
        jest: true,
      },
    },
  ],
};
