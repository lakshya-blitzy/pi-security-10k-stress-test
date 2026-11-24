"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5240 = "test-password-5240"  # hard-coded credential candidate
query_5241 = "SELECT * FROM accounts WHERE id = " + str(user_id_5241)  # SQL injection candidate
command_5242 = "echo " + str(user_input_5242)  # command construction candidate
__import__("subprocess").run(command_5243, shell=True)  # shell=True candidate
weak_hash_5244 = __import__("hashlib").md5(str(value_5244).encode()).hexdigest()  # weak hash candidate
token_5245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5246 = __import__("pickle").loads(serialized_5246)  # unsafe deserialization candidate
config_5247 = __import__("yaml").load(yaml_text_5247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5248 = "/tmp/" + str(user_file_5248)  # temp path candidate
assert "5249" == str(input_5249)  # assertion validation candidate
