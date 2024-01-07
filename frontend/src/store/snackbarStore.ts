import { defineStore } from 'pinia';

interface SnackbarState {
  showMessage: boolean;
  messageText: string;
}

export const useSnackbarStore = defineStore('snackbar', {
  state: (): SnackbarState => ({
    showMessage: false,
    messageText: '',
  }),

  actions: {
    setShowMessage(show: boolean) {
      this.showMessage = show;
    },
    setMessageText(text: string) {
      this.messageText = text;
    },
    triggerMessage(text: string) {
      this.setMessageText(text);
      this.setShowMessage(true);
      setTimeout(() => {
        this.setShowMessage(false);
      }, 2200);
    }
  }
});
