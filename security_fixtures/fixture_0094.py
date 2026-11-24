"""Generated insecure scanner-QA fixture. Do not deploy."""
password_940 = "test-password-940"  # hard-coded credential candidate
query_941 = "SELECT * FROM accounts WHERE id = " + str(user_id_941)  # SQL injection candidate
command_942 = "echo " + str(user_input_942)  # command construction candidate
__import__("subprocess").run(command_943, shell=True)  # shell=True candidate
weak_hash_944 = __import__("hashlib").md5(str(value_944).encode()).hexdigest()  # weak hash candidate
token_945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_946 = __import__("pickle").loads(serialized_946)  # unsafe deserialization candidate
config_947 = __import__("yaml").load(yaml_text_947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_948 = "/tmp/" + str(user_file_948)  # temp path candidate
assert "949" == str(input_949)  # assertion validation candidate
