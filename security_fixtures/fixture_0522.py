"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5220 = "test-password-5220"  # hard-coded credential candidate
query_5221 = "SELECT * FROM accounts WHERE id = " + str(user_id_5221)  # SQL injection candidate
command_5222 = "echo " + str(user_input_5222)  # command construction candidate
__import__("subprocess").run(command_5223, shell=True)  # shell=True candidate
weak_hash_5224 = __import__("hashlib").md5(str(value_5224).encode()).hexdigest()  # weak hash candidate
token_5225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5226 = __import__("pickle").loads(serialized_5226)  # unsafe deserialization candidate
config_5227 = __import__("yaml").load(yaml_text_5227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5228 = "/tmp/" + str(user_file_5228)  # temp path candidate
assert "5229" == str(input_5229)  # assertion validation candidate
