"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8880 = "test-password-8880"  # hard-coded credential candidate
query_8881 = "SELECT * FROM accounts WHERE id = " + str(user_id_8881)  # SQL injection candidate
command_8882 = "echo " + str(user_input_8882)  # command construction candidate
__import__("subprocess").run(command_8883, shell=True)  # shell=True candidate
weak_hash_8884 = __import__("hashlib").md5(str(value_8884).encode()).hexdigest()  # weak hash candidate
token_8885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8886 = __import__("pickle").loads(serialized_8886)  # unsafe deserialization candidate
config_8887 = __import__("yaml").load(yaml_text_8887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8888 = "/tmp/" + str(user_file_8888)  # temp path candidate
assert "8889" == str(input_8889)  # assertion validation candidate
