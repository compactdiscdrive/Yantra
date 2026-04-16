export const ssr = false;

import { redirect } from '@sveltejs/kit';
import { auth } from '$lib/firebase';

export const load = async () => {
  await auth.authStateReady();
  if (!auth.currentUser) {
    throw redirect(302, '/');
  }
};