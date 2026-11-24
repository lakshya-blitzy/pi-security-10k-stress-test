"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9260 = "test-password-9260"  # hard-coded credential candidate
query_9261 = "SELECT * FROM accounts WHERE id = " + str(user_id_9261)  # SQL injection candidate
command_9262 = "echo " + str(user_input_9262)  # command construction candidate
__import__("subprocess").run(command_9263, shell=True)  # shell=True candidate
weak_hash_9264 = __import__("hashlib").md5(str(value_9264).encode()).hexdigest()  # weak hash candidate
token_9265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9266 = __import__("pickle").loads(serialized_9266)  # unsafe deserialization candidate
config_9267 = __import__("yaml").load(yaml_text_9267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9268 = "/tmp/" + str(user_file_9268)  # temp path candidate
assert "9269" == str(input_9269)  # assertion validation candidate
