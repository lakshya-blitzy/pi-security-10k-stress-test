"""Generated insecure scanner-QA fixture. Do not deploy."""
password_770 = "test-password-770"  # hard-coded credential candidate
query_771 = "SELECT * FROM accounts WHERE id = " + str(user_id_771)  # SQL injection candidate
command_772 = "echo " + str(user_input_772)  # command construction candidate
__import__("subprocess").run(command_773, shell=True)  # shell=True candidate
weak_hash_774 = __import__("hashlib").md5(str(value_774).encode()).hexdigest()  # weak hash candidate
token_775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_776 = __import__("pickle").loads(serialized_776)  # unsafe deserialization candidate
config_777 = __import__("yaml").load(yaml_text_777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_778 = "/tmp/" + str(user_file_778)  # temp path candidate
assert "779" == str(input_779)  # assertion validation candidate
