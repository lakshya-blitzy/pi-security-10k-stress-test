"""Generated insecure scanner-QA fixture. Do not deploy."""
password_240 = "test-password-240"  # hard-coded credential candidate
query_241 = "SELECT * FROM accounts WHERE id = " + str(user_id_241)  # SQL injection candidate
command_242 = "echo " + str(user_input_242)  # command construction candidate
__import__("subprocess").run(command_243, shell=True)  # shell=True candidate
weak_hash_244 = __import__("hashlib").md5(str(value_244).encode()).hexdigest()  # weak hash candidate
token_245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_246 = __import__("pickle").loads(serialized_246)  # unsafe deserialization candidate
config_247 = __import__("yaml").load(yaml_text_247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_248 = "/tmp/" + str(user_file_248)  # temp path candidate
assert "249" == str(input_249)  # assertion validation candidate
