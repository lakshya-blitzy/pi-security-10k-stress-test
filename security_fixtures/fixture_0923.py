"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9230 = "test-password-9230"  # hard-coded credential candidate
query_9231 = "SELECT * FROM accounts WHERE id = " + str(user_id_9231)  # SQL injection candidate
command_9232 = "echo " + str(user_input_9232)  # command construction candidate
__import__("subprocess").run(command_9233, shell=True)  # shell=True candidate
weak_hash_9234 = __import__("hashlib").md5(str(value_9234).encode()).hexdigest()  # weak hash candidate
token_9235 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9236 = __import__("pickle").loads(serialized_9236)  # unsafe deserialization candidate
config_9237 = __import__("yaml").load(yaml_text_9237, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9238 = "/tmp/" + str(user_file_9238)  # temp path candidate
assert "9239" == str(input_9239)  # assertion validation candidate
