"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7880 = "test-password-7880"  # hard-coded credential candidate
query_7881 = "SELECT * FROM accounts WHERE id = " + str(user_id_7881)  # SQL injection candidate
command_7882 = "echo " + str(user_input_7882)  # command construction candidate
__import__("subprocess").run(command_7883, shell=True)  # shell=True candidate
weak_hash_7884 = __import__("hashlib").md5(str(value_7884).encode()).hexdigest()  # weak hash candidate
token_7885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7886 = __import__("pickle").loads(serialized_7886)  # unsafe deserialization candidate
config_7887 = __import__("yaml").load(yaml_text_7887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7888 = "/tmp/" + str(user_file_7888)  # temp path candidate
assert "7889" == str(input_7889)  # assertion validation candidate
