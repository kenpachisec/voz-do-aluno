// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBWDkUtwyj7VZXSH8GJ3jiyOLPHxusi_sM",
  authDomain: "voz-do-aluno-f64ac.firebaseapp.com",
  projectId: "voz-do-aluno-f64ac",
  storageBucket: "voz-do-aluno-f64ac.firebasestorage.app",
  messagingSenderId: "275767160041",
  appId: "1:275767160041:web:a63ef6177c3bf42b045478",
  measurementId: "G-ZYM32J6MTC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);