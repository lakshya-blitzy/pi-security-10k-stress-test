"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2770 = "test-password-2770"  # hard-coded credential candidate
query_2771 = "SELECT * FROM accounts WHERE id = " + str(user_id_2771)  # SQL injection candidate
command_2772 = "echo " + str(user_input_2772)  # command construction candidate
__import__("subprocess").run(command_2773, shell=True)  # shell=True candidate
weak_hash_2774 = __import__("hashlib").md5(str(value_2774).encode()).hexdigest()  # weak hash candidate
token_2775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2776 = __import__("pickle").loads(serialized_2776)  # unsafe deserialization candidate
config_2777 = __import__("yaml").load(yaml_text_2777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2778 = "/tmp/" + str(user_file_2778)  # temp path candidate
assert "2779" == str(input_2779)  # assertion validation candidate
