"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9770 = "test-password-9770"  # hard-coded credential candidate
query_9771 = "SELECT * FROM accounts WHERE id = " + str(user_id_9771)  # SQL injection candidate
command_9772 = "echo " + str(user_input_9772)  # command construction candidate
__import__("subprocess").run(command_9773, shell=True)  # shell=True candidate
weak_hash_9774 = __import__("hashlib").md5(str(value_9774).encode()).hexdigest()  # weak hash candidate
token_9775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9776 = __import__("pickle").loads(serialized_9776)  # unsafe deserialization candidate
config_9777 = __import__("yaml").load(yaml_text_9777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9778 = "/tmp/" + str(user_file_9778)  # temp path candidate
assert "9779" == str(input_9779)  # assertion validation candidate
