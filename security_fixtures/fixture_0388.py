"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3880 = "test-password-3880"  # hard-coded credential candidate
query_3881 = "SELECT * FROM accounts WHERE id = " + str(user_id_3881)  # SQL injection candidate
command_3882 = "echo " + str(user_input_3882)  # command construction candidate
__import__("subprocess").run(command_3883, shell=True)  # shell=True candidate
weak_hash_3884 = __import__("hashlib").md5(str(value_3884).encode()).hexdigest()  # weak hash candidate
token_3885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3886 = __import__("pickle").loads(serialized_3886)  # unsafe deserialization candidate
config_3887 = __import__("yaml").load(yaml_text_3887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3888 = "/tmp/" + str(user_file_3888)  # temp path candidate
assert "3889" == str(input_3889)  # assertion validation candidate
