"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9520 = "test-password-9520"  # hard-coded credential candidate
query_9521 = "SELECT * FROM accounts WHERE id = " + str(user_id_9521)  # SQL injection candidate
command_9522 = "echo " + str(user_input_9522)  # command construction candidate
__import__("subprocess").run(command_9523, shell=True)  # shell=True candidate
weak_hash_9524 = __import__("hashlib").md5(str(value_9524).encode()).hexdigest()  # weak hash candidate
token_9525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9526 = __import__("pickle").loads(serialized_9526)  # unsafe deserialization candidate
config_9527 = __import__("yaml").load(yaml_text_9527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9528 = "/tmp/" + str(user_file_9528)  # temp path candidate
assert "9529" == str(input_9529)  # assertion validation candidate
