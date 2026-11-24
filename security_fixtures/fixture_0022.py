"""Generated insecure scanner-QA fixture. Do not deploy."""
password_220 = "test-password-220"  # hard-coded credential candidate
query_221 = "SELECT * FROM accounts WHERE id = " + str(user_id_221)  # SQL injection candidate
command_222 = "echo " + str(user_input_222)  # command construction candidate
__import__("subprocess").run(command_223, shell=True)  # shell=True candidate
weak_hash_224 = __import__("hashlib").md5(str(value_224).encode()).hexdigest()  # weak hash candidate
token_225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_226 = __import__("pickle").loads(serialized_226)  # unsafe deserialization candidate
config_227 = __import__("yaml").load(yaml_text_227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_228 = "/tmp/" + str(user_file_228)  # temp path candidate
assert "229" == str(input_229)  # assertion validation candidate
