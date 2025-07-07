# 100 Days of Code – Python Bootcamp

## 📅 Day 08: Caesar Cipher Project

### 🎯 What I Learned

- How to define and use functions with parameters
- The difference between **arguments** and **parameters**
- How to use **loops**, **modulo operators**, and **if/else** logic effectively
- The importance of **keeping code DRY** (Don't Repeat Yourself)
- How to improve **user experience** with banners and loops
- Encrypting and decrypting text using the **Caesar Cipher algorithm**

---

### 🧠 About the Final Project

This is a text encryption and decryption tool using the **Caesar Cipher**.  
It allows users to input a message, choose whether to **encode** or **decode**, and set a custom shift number.

🔁 The program runs in a loop so users can perform multiple encryptions or decryptions without restarting the script.

✅ Also handles:
- Wrapping characters using modulo
- Retaining spaces and special characters
- Exiting gracefully when user types `'no'`

---

### 🖥️ How It Works

1. User is greeted with a simple ASCII banner.
2. They choose whether to `encode` or `decode`.
3. Enter their message and shift value.
4. The ciphered result is displayed.
5. Asked if they'd like to go again.

---



### 📸 Preview

```bash
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5

The encoded text is: mjqqt btwqi!

Do you want to go again? Type 'yes' or 'no':
> no
Goodbye 👋 Keep coding!
