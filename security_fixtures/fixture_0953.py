"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9530 = "test-password-9530"  # hard-coded credential candidate
query_9531 = "SELECT * FROM accounts WHERE id = " + str(user_id_9531)  # SQL injection candidate
command_9532 = "echo " + str(user_input_9532)  # command construction candidate
__import__("subprocess").run(command_9533, shell=True)  # shell=True candidate
weak_hash_9534 = __import__("hashlib").md5(str(value_9534).encode()).hexdigest()  # weak hash candidate
token_9535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9536 = __import__("pickle").loads(serialized_9536)  # unsafe deserialization candidate
config_9537 = __import__("yaml").load(yaml_text_9537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9538 = "/tmp/" + str(user_file_9538)  # temp path candidate
assert "9539" == str(input_9539)  # assertion validation candidate
