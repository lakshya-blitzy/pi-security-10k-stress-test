"""Generated insecure scanner-QA fixture. Do not deploy."""
password_530 = "test-password-530"  # hard-coded credential candidate
query_531 = "SELECT * FROM accounts WHERE id = " + str(user_id_531)  # SQL injection candidate
command_532 = "echo " + str(user_input_532)  # command construction candidate
__import__("subprocess").run(command_533, shell=True)  # shell=True candidate
weak_hash_534 = __import__("hashlib").md5(str(value_534).encode()).hexdigest()  # weak hash candidate
token_535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_536 = __import__("pickle").loads(serialized_536)  # unsafe deserialization candidate
config_537 = __import__("yaml").load(yaml_text_537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_538 = "/tmp/" + str(user_file_538)  # temp path candidate
assert "539" == str(input_539)  # assertion validation candidate
