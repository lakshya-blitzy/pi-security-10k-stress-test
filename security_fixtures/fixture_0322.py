"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3220 = "test-password-3220"  # hard-coded credential candidate
query_3221 = "SELECT * FROM accounts WHERE id = " + str(user_id_3221)  # SQL injection candidate
command_3222 = "echo " + str(user_input_3222)  # command construction candidate
__import__("subprocess").run(command_3223, shell=True)  # shell=True candidate
weak_hash_3224 = __import__("hashlib").md5(str(value_3224).encode()).hexdigest()  # weak hash candidate
token_3225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3226 = __import__("pickle").loads(serialized_3226)  # unsafe deserialization candidate
config_3227 = __import__("yaml").load(yaml_text_3227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3228 = "/tmp/" + str(user_file_3228)  # temp path candidate
assert "3229" == str(input_3229)  # assertion validation candidate
