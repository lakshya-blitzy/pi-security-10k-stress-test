"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5880 = "test-password-5880"  # hard-coded credential candidate
query_5881 = "SELECT * FROM accounts WHERE id = " + str(user_id_5881)  # SQL injection candidate
command_5882 = "echo " + str(user_input_5882)  # command construction candidate
__import__("subprocess").run(command_5883, shell=True)  # shell=True candidate
weak_hash_5884 = __import__("hashlib").md5(str(value_5884).encode()).hexdigest()  # weak hash candidate
token_5885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5886 = __import__("pickle").loads(serialized_5886)  # unsafe deserialization candidate
config_5887 = __import__("yaml").load(yaml_text_5887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5888 = "/tmp/" + str(user_file_5888)  # temp path candidate
assert "5889" == str(input_5889)  # assertion validation candidate
