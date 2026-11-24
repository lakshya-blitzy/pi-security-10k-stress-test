"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6890 = "test-password-6890"  # hard-coded credential candidate
query_6891 = "SELECT * FROM accounts WHERE id = " + str(user_id_6891)  # SQL injection candidate
command_6892 = "echo " + str(user_input_6892)  # command construction candidate
__import__("subprocess").run(command_6893, shell=True)  # shell=True candidate
weak_hash_6894 = __import__("hashlib").md5(str(value_6894).encode()).hexdigest()  # weak hash candidate
token_6895 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6896 = __import__("pickle").loads(serialized_6896)  # unsafe deserialization candidate
config_6897 = __import__("yaml").load(yaml_text_6897, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6898 = "/tmp/" + str(user_file_6898)  # temp path candidate
assert "6899" == str(input_6899)  # assertion validation candidate
