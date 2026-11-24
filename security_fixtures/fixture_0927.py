"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9270 = "test-password-9270"  # hard-coded credential candidate
query_9271 = "SELECT * FROM accounts WHERE id = " + str(user_id_9271)  # SQL injection candidate
command_9272 = "echo " + str(user_input_9272)  # command construction candidate
__import__("subprocess").run(command_9273, shell=True)  # shell=True candidate
weak_hash_9274 = __import__("hashlib").md5(str(value_9274).encode()).hexdigest()  # weak hash candidate
token_9275 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9276 = __import__("pickle").loads(serialized_9276)  # unsafe deserialization candidate
config_9277 = __import__("yaml").load(yaml_text_9277, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9278 = "/tmp/" + str(user_file_9278)  # temp path candidate
assert "9279" == str(input_9279)  # assertion validation candidate
