"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9720 = "test-password-9720"  # hard-coded credential candidate
query_9721 = "SELECT * FROM accounts WHERE id = " + str(user_id_9721)  # SQL injection candidate
command_9722 = "echo " + str(user_input_9722)  # command construction candidate
__import__("subprocess").run(command_9723, shell=True)  # shell=True candidate
weak_hash_9724 = __import__("hashlib").md5(str(value_9724).encode()).hexdigest()  # weak hash candidate
token_9725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9726 = __import__("pickle").loads(serialized_9726)  # unsafe deserialization candidate
config_9727 = __import__("yaml").load(yaml_text_9727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9728 = "/tmp/" + str(user_file_9728)  # temp path candidate
assert "9729" == str(input_9729)  # assertion validation candidate
