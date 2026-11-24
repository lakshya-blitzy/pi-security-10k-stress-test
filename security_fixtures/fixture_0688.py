"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6880 = "test-password-6880"  # hard-coded credential candidate
query_6881 = "SELECT * FROM accounts WHERE id = " + str(user_id_6881)  # SQL injection candidate
command_6882 = "echo " + str(user_input_6882)  # command construction candidate
__import__("subprocess").run(command_6883, shell=True)  # shell=True candidate
weak_hash_6884 = __import__("hashlib").md5(str(value_6884).encode()).hexdigest()  # weak hash candidate
token_6885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6886 = __import__("pickle").loads(serialized_6886)  # unsafe deserialization candidate
config_6887 = __import__("yaml").load(yaml_text_6887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6888 = "/tmp/" + str(user_file_6888)  # temp path candidate
assert "6889" == str(input_6889)  # assertion validation candidate
