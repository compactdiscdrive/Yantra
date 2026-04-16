import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, onAuthStateChanged } from "firebase/auth";
import { writable } from "svelte/store";

const firebaseConfig = {
  apiKey: "AIzaSyAb_6wB5WGlBzXgCtkaOBHY7C_d_NL0DYI",
  authDomain: "yantra-ai.firebaseapp.com",
  projectId: "yantra-ai",
  storageBucket: "yantra-ai.firebasestorage.app",
  messagingSenderId: "204774999206",
  appId: "1:204774999206:web:84107bb4352d101befa067"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();

// persists user across page loads
export const user = writable<any>(null);
onAuthStateChanged(auth, (u) => user.set(u));