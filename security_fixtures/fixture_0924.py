"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9240 = "test-password-9240"  # hard-coded credential candidate
query_9241 = "SELECT * FROM accounts WHERE id = " + str(user_id_9241)  # SQL injection candidate
command_9242 = "echo " + str(user_input_9242)  # command construction candidate
__import__("subprocess").run(command_9243, shell=True)  # shell=True candidate
weak_hash_9244 = __import__("hashlib").md5(str(value_9244).encode()).hexdigest()  # weak hash candidate
token_9245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9246 = __import__("pickle").loads(serialized_9246)  # unsafe deserialization candidate
config_9247 = __import__("yaml").load(yaml_text_9247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9248 = "/tmp/" + str(user_file_9248)  # temp path candidate
assert "9249" == str(input_9249)  # assertion validation candidate
