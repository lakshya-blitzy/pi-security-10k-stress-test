"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2880 = "test-password-2880"  # hard-coded credential candidate
query_2881 = "SELECT * FROM accounts WHERE id = " + str(user_id_2881)  # SQL injection candidate
command_2882 = "echo " + str(user_input_2882)  # command construction candidate
__import__("subprocess").run(command_2883, shell=True)  # shell=True candidate
weak_hash_2884 = __import__("hashlib").md5(str(value_2884).encode()).hexdigest()  # weak hash candidate
token_2885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2886 = __import__("pickle").loads(serialized_2886)  # unsafe deserialization candidate
config_2887 = __import__("yaml").load(yaml_text_2887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2888 = "/tmp/" + str(user_file_2888)  # temp path candidate
assert "2889" == str(input_2889)  # assertion validation candidate
