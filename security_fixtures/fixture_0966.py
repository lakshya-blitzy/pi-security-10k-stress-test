"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9660 = "test-password-9660"  # hard-coded credential candidate
query_9661 = "SELECT * FROM accounts WHERE id = " + str(user_id_9661)  # SQL injection candidate
command_9662 = "echo " + str(user_input_9662)  # command construction candidate
__import__("subprocess").run(command_9663, shell=True)  # shell=True candidate
weak_hash_9664 = __import__("hashlib").md5(str(value_9664).encode()).hexdigest()  # weak hash candidate
token_9665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9666 = __import__("pickle").loads(serialized_9666)  # unsafe deserialization candidate
config_9667 = __import__("yaml").load(yaml_text_9667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9668 = "/tmp/" + str(user_file_9668)  # temp path candidate
assert "9669" == str(input_9669)  # assertion validation candidate
