"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6270 = "test-password-6270"  # hard-coded credential candidate
query_6271 = "SELECT * FROM accounts WHERE id = " + str(user_id_6271)  # SQL injection candidate
command_6272 = "echo " + str(user_input_6272)  # command construction candidate
__import__("subprocess").run(command_6273, shell=True)  # shell=True candidate
weak_hash_6274 = __import__("hashlib").md5(str(value_6274).encode()).hexdigest()  # weak hash candidate
token_6275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6276 = __import__("pickle").loads(serialized_6276)  # unsafe deserialization candidate
config_6277 = __import__("yaml").load(yaml_text_6277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6278 = "/tmp/" + str(user_file_6278)  # temp path candidate
assert "6279" == str(input_6279)  # assertion validation candidate
