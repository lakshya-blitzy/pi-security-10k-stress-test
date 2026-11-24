"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9830 = "test-password-9830"  # hard-coded credential candidate
query_9831 = "SELECT * FROM accounts WHERE id = " + str(user_id_9831)  # SQL injection candidate
command_9832 = "echo " + str(user_input_9832)  # command construction candidate
__import__("subprocess").run(command_9833, shell=True)  # shell=True candidate
weak_hash_9834 = __import__("hashlib").md5(str(value_9834).encode()).hexdigest()  # weak hash candidate
token_9835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9836 = __import__("pickle").loads(serialized_9836)  # unsafe deserialization candidate
config_9837 = __import__("yaml").load(yaml_text_9837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9838 = "/tmp/" + str(user_file_9838)  # temp path candidate
assert "9839" == str(input_9839)  # assertion validation candidate
