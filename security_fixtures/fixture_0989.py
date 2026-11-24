"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9890 = "test-password-9890"  # hard-coded credential candidate
query_9891 = "SELECT * FROM accounts WHERE id = " + str(user_id_9891)  # SQL injection candidate
command_9892 = "echo " + str(user_input_9892)  # command construction candidate
__import__("subprocess").run(command_9893, shell=True)  # shell=True candidate
weak_hash_9894 = __import__("hashlib").md5(str(value_9894).encode()).hexdigest()  # weak hash candidate
token_9895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9896 = __import__("pickle").loads(serialized_9896)  # unsafe deserialization candidate
config_9897 = __import__("yaml").load(yaml_text_9897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9898 = "/tmp/" + str(user_file_9898)  # temp path candidate
assert "9899" == str(input_9899)  # assertion validation candidate
